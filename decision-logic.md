flowchart TD
    A[Start: Employee evaluated this quarter] --> B{Predicted retention risk high?}

    B -- No (risk not high) --> G{Perf above target AND PsychSafety >= 8?}
    B -- Yes (high risk) --> C{PsychSafety < 7?}

    C -- Yes (low safety) --> D{Current SupportType?}
    C -- No (safety ok) --> E{Performance below target?}

    D -- None or Light --> D1[Action A1: Enroll in structured support<br/>+ Safety-focused manager 1:1<br/>+ Flag for next-quarter review]
    D -- Structured --> D2[Action A2: Review support quality<br/>+ Escalate to People/HR if risk persists]

    E -- Yes (underperforming) --> E1[Action B1: Keep support level<br/>+ Performance coaching plan<br/>+ Increase manager 1:1 cadence]
    E -- No (performance fine) --> E2[Action B2: Monitor only<br/>+ Manager wellbeing check-in]

    G -- Yes (thriving) --> G1[Action C1: Maintain support<br/>+ Offer stretch/mentoring opportunities]
    G -- No (steady) --> G2[Action C2: Maintain support<br/>+ Monitor via regular cycle]

    %% Optional tenure nuance
    D1 --> T{Tenure < 6 months?}
    E1 --> T

    T -- Yes (new hire) --> T1[Frame plan as onboarding / ramp support]
    T -- No (established) --> T2[Frame plan as development / growth plan]

    D1 --> H[End: Decision documented & next review scheduled]
    D2 --> H
    E1 --> H
    E2 --> H
    G1 --> H
    G2 --> H
    T1 --> H
    T2 --> H
