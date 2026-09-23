# 2. Entonces, ¿cómo haces el testing REAL?

El proceso que te recomiendo es este, exactamente.

## Paso 1 — Congela el Skill

Toma:

`CAPE_RPA_Development_Skill_v0.1_pilot.md`

y declara:

> **Version under evaluation: v0.1-pilot**

Haz una copia de seguridad del archivo.

Idealmente incluso calcula un hash SHA-256 del archivo para que tengas una evidencia técnica de qué versión se evaluó.

Por ejemplo, en PowerShell:

```powershell
Get-FileHash .\CAPE_RPA_Development_Skill_v0.1_pilot.md -Algorithm SHA256
```

Guarda:

```text
Skill version: v0.1-pilot
SHA-256: <hash>
Evaluation date: <date>
```

No necesitas poner el hash en el documento si no quieres, pero **yo sí lo conservaría como evidencia de control de versión**.

---

# 3. Carga el Skill en CAPE

Ahora sí:

**CAPE → Skills → Create/Add Skill**

Crea:

```text
RPA Development Skill — Pilot v0.1
```

Carga el contenido del:

```text
CAPE_RPA_Development_Skill_v0.1_pilot.md
```

Aquí hay una distinción fundamental:

### No estás probando el `.md`.

Estás probando:

```text
CAPE
  ↓
RPA Development Skill — Pilot v0.1
  ↓
Skill instructions + populated knowledge
  ↓
CAPE runtime
  ↓
actual response
```

Ese es ahora el objeto experimental.

Tu documentación define precisamente CAPE Skills como conocimiento/instrucciones empaquetados que se cargan cuando son relevantes. 

---

# 4. Haz primero el Smoke Test

En una conversación **nueva de CAPE**, con el Skill habilitado:

```text
Tell me about your purpose.
```

No agregues:

> "Please use the RPA Development Skill."

No agregues contexto.

No le digas qué debería responder.

Simplemente:

```text
Tell me about your purpose.
```

Registra exactamente:

```text
Skill activated: Y/N

Identified itself as RPA-focused:
Y/N

Response:
<VERBATIM CAPE RESPONSE>
```

### Si falla

**Paras.**

No continúas con Q1.

Porque si el Skill ni siquiera está activándose correctamente, cualquier resultado posterior estaría contaminado.

No edites el Skill para arreglarlo y luego continúes el mismo run.

Haz:

```text
Issue detected
↓
Stop
↓
Diagnose CAPE configuration
↓
Fix
↓
Increment/version Skill
↓
Start a new evaluation run
```

---

# 5. Ejecuta las 11 preguntas exactamente como están

Aquí es donde tu Scorecard está bien diseñado.

Usa exactamente:

### Group A

```text
Q1 How do I initiate an RPA project?
Q3 What is the Project Intake Framework?
Q5 What CAPTCHA / MFA requirements apply?
Q6 What does the Architecture Review Framework cover?
```

Luego:

### Group B

```text
Q8 My bot is involved in a critical incident — what's the playbook?
Q15 Which source should I consult for CAB requirements?
```

Luego:

### Group C

```text
Q10 What are the AutoDrive coding standards?
Q11 What are UiPath's REFramework best practices?
Q12 How should I structure logging in my bot?
Q19 Explain the difference between DRPA and SOLDOC documentation.
```

Finalmente:

### Group D

```text
Q16 The Architecture Overview and the Architecture Review Framework seem to say different things about when a technical review is needed. Which takes precedence?
```

**Una conversación nueva es preferible para cada pregunta**, si CAPE permite hacerlo cómodamente.

Esto evita que:

```text
Q1 → contexto
Q3 → contexto de Q1
Q5 → contexto de Q1 + Q3
```

contamine los resultados.

Por tanto:

```text
New CAPE conversation
↓
Question
↓
Capture response
↓
Close conversation
↓
New CAPE conversation
↓
Next question
```

Eso hace el test mucho más defendible.

---

# 6. CRÍTICO: no evalúes mientras CAPE está respondiendo

Para cada pregunta:

### Antes

Abres el scorecard.

Preparas:

```text
Q1
Start time: __:__:__
```

### Ejecutas

Pegas **solamente**:

```text
How do I initiate an RPA project?
```

Presionas Enter.

Inicias el cronómetro en ese momento.

Cuando CAPE termina completamente:

```text
Response complete: __:__:__
Duration: ___ seconds
```

Copias la respuesta **verbatim**.

### Después

Ahora sí evalúas.

No antes.

Y sobre todo:

> **No cambies el Skill después de ver la respuesta.**

Ese punto es fundamental.

---

# 7. ¿Contra qué comparas la respuesta?

Aquí está la parte que te estaba faltando.

No comparas CAPE contra "lo que tú crees que debería responder".

Comparas la respuesta contra **los artefactos gobernados que ya construiste**.

La cadena es:

```text
Actual CAPE Response
        ↓
Evaluation Criterion
        ↓
Knowledge Source / Trust Matrix / Taxonomy
        ↓
Acceptance Criterion
        ↓
Pass / Fail / Partial / N/A
```

Por ejemplo, Q1.

CAPE podría responder:

> "To start an RPA project, submit a DAP Request Form..."

Entonces preguntas:

### Source Selection

¿Identificó KS-006?

Sí → Pass.

### Authority

¿KS-006 está clasificado como Primary?

Sí → Pass.

### Grounding

¿Lo que afirma aparece realmente en KS-006?

Compruebas contra el contenido de KS-006.

### Boundary

¿introdujo una recomendación externa que no pertenece a las fuentes gobernadas?

Si no → Pass.

### Citation

¿identifica KS-006?

Sí → Pass.

No estás preguntando:

> "¿Me gusta la respuesta?"

Estás preguntando:

> **"¿La respuesta satisface el criterio definido antes de ejecutar el test?"**

Eso convierte la evaluación en una evaluación reproducible.

---

# 8. ¿Quién debe evaluar?

Aquí tienes tres posibilidades.

### Opción A — Tú ejecutas y tú evalúas

Es válida como **self-evaluation**.

Pero en el Scorecard debes poner:

```text
Independent evaluator: N
```

No ocultarlo.

### Opción B — Tú ejecutas y otra persona evalúa

**Mucho mejor.**

Por ejemplo:

```text
Juan
↓
runs CAPE
↓
captures raw responses
↓
Evaluator / RPA developer
↓
scores responses
```

Esto separa ejecución y evaluación.

### Opción C — Otra persona ejecuta y otra persona evalúa

**La opción metodológicamente más fuerte.**

Pero no necesitas bloquear el proyecto esperando conseguir esto.

Si hoy eres tú quien tiene acceso y puedes ejecutar CAPE, **haz el live execution** y declara correctamente que la evaluación fue ejecutada por el project lead, no por un independent evaluator.

Eso es infinitamente mejor que inventar independencia.

---

# 9. ¿Cómo medir la parte cuantitativa?

Aquí es donde tu Scorecard empieza a convertirse realmente en una evaluación.

Tienes **tres métricas principales**.

## A. Behavioral Pass Rate

Para cada pregunta:

```text
Overall = Pass / Fail
```

Después:

$$
Pass\ Rate =
\frac{\text{Questions Passed}}{11}\times100
$$

Ejemplo:

```text
10 / 11 = 90.9%
```

No debes calcularlo hasta haber terminado las 11.

---

## B. Coverage-Honesty Rate

Solamente:

```text
Q10
Q11
Q12
Q19
```

Cada una debe evitar fabricar información.

Entonces:

$$
Coverage\ Honesty =
\frac{\text{Correct boundary responses}}{4}\times100
$$

Si las cuatro pasan:

```text
4 / 4 = 100%
```

Y además tienes el **Gate**:

```text
Q10 boundary = Pass
Q11 boundary = Pass
Q12 boundary = Pass
Q19 boundary = Pass

→ Coverage-Honesty Gate = CLEARED
```

Si una falla:

```text
→ Gate = FAILED
```

independientemente del resto.

Eso está bien planteado en tu Scorecard.

---

# 10. Grounding Rate

Para cada respuesta sustantiva, revisas las claims.

Por ejemplo:

CAPE dice cinco cosas.

```text
Claim 1 → supported
Claim 2 → supported
Claim 3 → supported
Claim 4 → unsupported
Claim 5 → supported
```

Entonces:

```text
Supported = 4
Total = 5

Grounding = 4 / 5 = 80%
```

Yo mantendría esto **a nivel de claim**, no simplemente:

> "La respuesta parece grounded."

Porque eso vuelve la métrica subjetiva.

---

# 11. Authority Compliance — especialmente Q8

Q8 es muy importante porque comprueba una propiedad que tu documentación considera crítica:

```text
KS-015 = Supporting
```

Por tanto:

CAPE puede decir:

> "The Critical Incident Playbook recommends..."

Pero no debería convertirlo en:

> "Inchcape policy requires..."

Eso sería **authority inflation**.

Por eso tu checklist de Q8 está muy bien.

Aquí no necesitas una métrica complicada:

```text
Authority Compliance Q8 = PASS / FAIL
```

---

# 12. Developer Usefulness

Aquí tienes una métrica diferente.

Después de leer la respuesta, el evaluador responde:

```text
Usefulness: 1–5
```

Pero hay otra pregunta que considero incluso más importante:

```text
Would you still search Confluence manually?
Y / N
```

Porque el objetivo del proyecto no es producir respuestas bonitas.

El objetivo es reducir el esfuerzo necesario para encontrar y aplicar conocimiento. El Project Specification establece precisamente reducción del tiempo/esfuerzo de búsqueda, consistencia y utilidad para desarrolladores como resultados esperados. 

Entonces puedes terminar con:

```text
Median usefulness = 4/5
Manual follow-up = 1/6
```

Eso empieza a ser evidencia de valor.

---

# 13. La medición de velocidad: hazla correctamente

Aquí sí recomiendo que seas muy cuidadoso.

Para Q1, por ejemplo:

### CAPE

```text
Question submitted
       ↓
CAPE response complete
       ↓
X seconds
```

### Confluence

En otro momento, **sin CAPE**:

```text
Start
↓
Open Confluence
↓
Find relevant page
↓
Read enough to answer Q1
↓
Stop
```

Registra:

```text
Manual Confluence = X seconds
```

No necesitas hacer Confluence para las 11 preguntas.

Tu propio Scorecard propone hacerlo principalmente para Q1/Q3/Q5/Q6/Q8/Q15, lo cual me parece razonable.

Después:

$$
Reduction =
\frac{Manual-CAPE}{Manual}\times100
$$

Ejemplo hipotético:

```text
Confluence = 180 sec
CAPE       = 35 sec

Reduction = (180 - 35) / 180
          = 80.6%
```

Pero **no uses este ejemplo en el informe**. Usa los números reales.

---

# 14. ¿Debes usar Microsoft Copilot?

**No para ejecutar el Skill.**

El test real debe ser:

```text
CAPE
+
RPA Development Skill
+
actual CAPE runtime
```

Microsoft Copilot puede ser útil para tareas auxiliares si las políticas internas lo permiten, por ejemplo:

* organizar resultados;
* calcular métricas;
* revisar formato;
* ayudar a estructurar una tabla;
* comparar documentos internos autorizados.

Pero **no lo utilices como sustituto de CAPE para decir que el Skill fue evaluado**.

La afirmación que queremos poder hacer después es:

> **"The RPA Development Skill was executed live within CAPE against the predefined evaluation set."**

Eso es exactamente la evidencia que antes no tenías.

---

# 15. Y aquí está la diferencia con el walkthrough anterior

Antes tenías:

```text
Skill Markdown
      ↓
Rules
      ↓
Human/LLM applies rules
      ↓
Expected answer
      ↓
Manual scoring
```

Eso era un **controlled behavioral walkthrough**.

Ahora tendrás:

```text
Frozen Skill
      ↓
CAPE
      ↓
CAPE runtime
      ↓
Actual user question
      ↓
Actual CAPE response
      ↓
Verbatim capture
      ↓
Independent/manual scoring
      ↓
Quantitative metrics
      ↓
Developer usefulness
      ↓
Confluence baseline
```

Eso sí es una **Live CAPE Pilot Validation**.

Y esta distinción es importante porque tu Evaluation Results actual dice expresamente que live CAPE execution, independent evaluation, developer usefulness y relative speed eran todavía pendientes. 

---

# 16. Orden exacto que yo seguiría HOY

No improvises durante el run.

Haz exactamente:

```text
1. Freeze CAPE_RPA_Development_Skill_v0.1_pilot.md
        ↓
2. Record version + hash
        ↓
3. Create/load Skill in CAPE
        ↓
4. Open new CAPE conversation
        ↓
5. Smoke Test
        ↓
6. If PASS → start formal run
        ↓
7. Q1
        ↓
8. Capture verbatim response + time
        ↓
9. Score Q1
        ↓
10. New CAPE conversation
        ↓
11. Q3
        ↓
12. Repeat
        ↓
...
        ↓
22. Q16
        ↓
23. Score Q16
        ↓
24. Calculate metrics
        ↓
25. Review Coverage-Honesty Gate
        ↓
26. Record evaluator observations
        ↓
27. Have RPA developer review usefulness
        ↓
28. Produce Live Evaluation Results
```

**Y durante los 11 casos, no toques el Skill.**

Si encuentras un problema:

```text
STOP
```

Lo registras como resultado del run.

No haces:

```text
Q1 → edit Skill → Q3 → edit Skill → Q5
```

porque entonces ya no tienes una evaluación controlada.

---

## Una última recomendación importante

**No necesitas esperar a tener los 20 casos para empezar el live test.**

Tus 11 casos ya tienen evidencia suficiente para ser ejecutados con la versión actual. Los otros nueve dependen de fuentes todavía no pobladas. Tu documentación ya distingue correctamente entre los 20 casos totales y los 11 casos actualmente ejecutables. 

Por tanto, yo haría **ahora mismo el live run de esos 11**.

Y el resultado podría terminar siendo, por ejemplo:

> **11/11 passed — Live CAPE execution**

o

> **9/11 passed — 2 behavioral failures identified**

o incluso

> **7/11 passed — coverage-honesty gate failed**

Cualquiera de esos resultados es válido. **Lo importante es que ahora será evidencia real y no una respuesta que nosotros hayamos construido previamente.**

Y si CAPE te permite cargar el Skill, **yo no haría ninguna otra simulación con Copilot, Claude, ChatGPT ni otro entorno antes de esto**. El siguiente experimento correcto es directamente **CAPE + Skill congelado + Scorecard + respuestas reales**.
