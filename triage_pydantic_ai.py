import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    [PydanticAI: the AI Agent Framework Winner](https://youtu.be/-WB0T0XmDrY?si=R-V9UZNrr51N7N45)

    - Set export OPENAI_API_KEY= on terminal before starting marimo
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import asyncio
    from dataclasses import dataclass
    from pydantic import BaseModel, Field
    from pydantic_ai import Agent, RunContext
    from typing import Any
    from dotenv import load_dotenv

    return Agent, Any, BaseModel, Field, RunContext, dataclass, load_dotenv


@app.cell
def _(load_dotenv):
    load_dotenv()
    return


@app.cell
def _(Any, dataclass):
    # Mock database
    @dataclass
    class Patient:
        id: int
        name: str
        vitals: dict[str, Any]

    PATIENT_DB: dict[int, Patient] = {
        1: Patient(id=1, name="Alice LowBP", vitals={"heart_rate": 72, "blood_pressure": "85/55"}),
        2: Patient(id=2, name="Bob NormalBP", vitals={"heart_rate": 78, "blood_pressure": "118/76"}),
        3: Patient(id=3, name="Charlie HighBP", vitals={"heart_rate": 88, "blood_pressure": "152/95"}),
        4: Patient(id=4, name="Diana LowBP", vitals={"heart_rate": 65, "blood_pressure": "90/58"}),
        5: Patient(id=5, name="Ethan NormalBP", vitals={"heart_rate": 80, "blood_pressure": "120/80"}),
        6: Patient(id=6, name="Fiona HighBP", vitals={"heart_rate": 92, "blood_pressure": "160/100"}),
        7: Patient(id=7, name="George LowBP", vitals={"heart_rate": 70, "blood_pressure": "88/60"}),
        8: Patient(id=8, name="Hannah NormalBP", vitals={"heart_rate": 75, "blood_pressure": "115/75"}),
        9: Patient(id=9, name="Ian HighBP", vitals={"heart_rate": 95, "blood_pressure": "170/105"}),
        10: Patient(id=10, name="Julia NormalBP", vitals={"heart_rate": 77, "blood_pressure": "122/78"}),
    }    
    return (PATIENT_DB,)


@app.cell
def _(PATIENT_DB: "dict[int, Patient]"):
    # Helper class
    class DatabaseConn:
        async def get_patient_name(self, id: int):
            patient = PATIENT_DB.get(id)
            return patient.name if patient else "Unkown Patient"

        async def get_patient_vitals(self, id: int):
            patient = PATIENT_DB.get(id)
            return patient.vitals if patient else "Unknown Patient"
    return (DatabaseConn,)


@app.cell
def _(Agent, BaseModel, DatabaseConn, Field, RunContext, dataclass):
    @dataclass
    class TriageDependencies:
        patient_id : int
        db: DatabaseConn

    class TriageOutput(BaseModel):
        response_text: str = Field(description="Message to patient from triage")
        escalate : bool = Field(description="Should we escalate to a hiuman?")
        urgency: int = Field(description="Integer showing urgency level")


    triage_agent = Agent(
        "openai:gpt-4o",
        deps_type=TriageDependencies,
        output_type=TriageOutput,
        system_prompt=(
            "You are a triage agent for a hospital to help the patients."
            "Provide clear advice and assess urgency level. "
            "Always mention the patients name if available."
        )
    )

    @triage_agent.system_prompt
    async def add_patient_name(ctx: RunContext[TriageDependencies])-> str:
        patient_name = await ctx.deps.db.get_patient_name(ctx.deps.patient_id)
        return f"The Patient Name is : {patient_name}"

    @triage_agent.tool
    async def get_latest_vitals(ctx: RunContext[TriageDependencies])-> str:
        return await ctx.deps.db.get_patient_vitals(ctx.deps.patient_id)

    return TriageDependencies, triage_agent


@app.cell
def _(DatabaseConn, TriageDependencies, triage_agent):
    async def main()-> None:
        db = DatabaseConn()

        # Test that the async functions
        patient_name = await db.get_patient_name(4)
        patient_vitals = await db.get_patient_vitals(4)

        print(f"""
            Name : {patient_name}
            Vitals : {patient_vitals}
            """)

        # Use Pydantic AI - Low BP
        deps = TriageDependencies(
            patient_id=4,
            db=db
        )

        result = await triage_agent.run(
            "What should I do if I have a headache and a fever?",
            deps=deps)
        print(result.output)
    

        # Use Pydantic AI - Normal BP
        deps = TriageDependencies(
            patient_id=2,
            db=db
        )

        result = await triage_agent.run(
            "What should I do if I have a headache and a fever?",
            deps=deps)
        print(result.output)

         # Use Pydantic AI - High BP
        deps = TriageDependencies(
            patient_id=3,
            db=db
        )

        result = await triage_agent.run(
            "What should I do if I have a headache and a fever?",
            deps=deps)
        print(result.output)   
    return (main,)


@app.cell
async def _(main):

    if __name__ == "__main__":
        # asyncio.run(main())
        await main()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
