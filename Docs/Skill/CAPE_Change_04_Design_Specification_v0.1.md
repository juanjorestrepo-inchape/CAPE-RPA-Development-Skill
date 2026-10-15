# Change 04 — KS-ID Provenance Traceability

**CAPE RPA Development Skill · Iteration 2 — Hardening · Design Specification v0.1 · 14 October 2026**

**Estado:** Diseño propuesto para revisión. La aprobación de alcance ya está registrada; esta entrega concreta los requisitos, las reglas de comportamiento y los criterios de aceptación. No modifica el Skill activo, no cambia la Trust Matrix y no inicia la regresión formal.

---

## 1. Contexto aplicado

El diseño se basa en los siguientes artefactos del proyecto:

- **Functional Specification v0.1 — Tranche 1:** Separa la elegibilidad de una fuente de su clasificación temática y exige que la respuesta sea trazable a la selección de fuentes (`RPA_Development_Skill_Functional_Specification_v0.1_Tranche1(1).docx`).
- **Trust Matrix v0.1:** Es la autoridad para `Permitted Use`, `Assessment Status` y `Source Role`; estos campos no deben deducirse de la taxonomía ni de la disponibilidad de una página (`RPA_Knowledge_Source_Trust_Matrix_v0.1(2).docx`).
- **Knowledge Taxonomy v0.1.1:** Organiza fuentes y dominios, pero no puede elevar la confianza ni cambiar la clasificación gobernada de una fuente (`RPA_Knowledge_Taxonomy_v0.1.1(1).docx`).
- **Implementation Record v0.1, revisión r1:** Define Change 04, sus siete casos de verificación y las limitaciones actuales de reconciliación de fuentes.

La limitación principal permanece vigente: hay siete fuentes pobladas y elegibles para el uso probatorio del piloto, pero los metadatos de clasificación de seis de ellas siguen sin reconciliarse a nivel de registro individual. KS-015 mantiene su ambigüedad de rol. Change 04 no debe resolver estos problemas por inferencia.

---

## 2. Objetivo y límite de la solución

**Objetivo:** Establecer una correspondencia verificable entre el contenido efectivamente recuperado, la identidad de su fuente gobernada y las afirmaciones que ese contenido respalda.

La trazabilidad debe permitir responder cuatro preguntas diferentes:

1. ¿Qué contenido se recuperó realmente?
2. ¿A qué página o recurso corresponde?
3. ¿Qué `KS-ID` y metadatos gobernados pueden asociarse a ese recurso con evidencia suficiente?
4. ¿Qué afirmaciones de la respuesta están respaldadas por ese contenido?

La solución debe distinguir entre la identidad técnica del recurso recuperado y su clasificación dentro de la Trust Matrix. Una página de Confluence puede identificarse técnicamente sin que eso resuelva si su rol gobernado es `Primary` o `Supporting`, ni si su contenido está autorizado para un uso específico.

**Fuera del alcance de Change 04:** Reconciliar la Trust Matrix, elegir entre páginas duplicadas sin una decisión gobernada, incorporar fuentes adicionales, cambiar el mecanismo de activación de CAPE o implementar una nueva arquitectura de recuperación.

---

## 3. Diseño funcional propuesto

```
1. Contenido recuperado
   └── Identificar el recurso real, su ubicación y los metadatos disponibles.
2. Resolución de identidad
   └── Vincular el recurso con un registro KS verificado; no inferir el ID por similitud de título.
3. Validación de gobernanza
   └── Comprobar rol, estado de evaluación, uso permitido y restricciones aplicables.
4. Evidencia y afirmaciones
   └── Vincular cada afirmación relevante con contenido que realmente la respalde.
5. Respuesta controlada
   └── Responder dentro de los límites demostrados o comunicar la limitación.
```

### 3.1 Identidad de la fuente

La identificación debe seguir esta prioridad:

1. Identificador estable del recurso recuperado, cuando el conector lo proporcione.
2. Registro gobernado que vincule ese identificador con un `KS-ID`.
3. Confirmación de que el recurso corresponde a la versión o ubicación autorizada, según los metadatos disponibles.
4. Asociación de los fragmentos recuperados con esa identidad verificada.

El título de la página, su contenido temático o su posición en los resultados de búsqueda pueden servir para localizar candidatos, pero no bastan para demostrar su identidad gobernada.

Para Confluence Cloud, la API oficial documenta identificadores de página y metadatos como título, espacio, estado y versión (`developer.atlassian.com`). Estos datos podrían servir como señales técnicas de identidad si están disponibles a través de la integración utilizada. Sin embargo, la documentación pública de Atlassian no demuestra que el conector actual de CAPE exponga todos esos campos.

### 3.2 Registro de procedencia

Cada recurso utilizado como evidencia debe poder asociarse al siguiente conjunto lógico de datos. Este es un contrato de información propuesto, no una afirmación de que todos los campos ya estén disponibles en CAPE.

| Campo | Requisito |
|---|---|
| `retrieved_resource_id` | Identificador técnico del recurso, si está disponible. |
| `resource_title` | Título devuelto por la fuente. |
| `resource_location` | URL, espacio o ubicación disponible para identificar el recurso. |
| `resource_version` | Versión o fecha de actualización, si se expone. |
| `ks_id` | Identificador gobernado verificado; nunca inferido por semejanza temática. |
| `source_role` | Valor del registro gobernado; mantener `UNVERIFIED` cuando corresponda. |
| `assessment_status` | Valor del registro gobernado; no sustituirlo por una conclusión del Skill. |
| `permitted_use` | Disposición de uso gobernada, con sus restricciones aplicables. |
| `evidence_reference` | Referencia al contenido recuperado que respalda la afirmación. |
| `verification_state` | Resultado de la comprobación de identidad y metadatos. |

Los campos no disponibles deben permanecer explícitamente desconocidos. No se deben completar con valores por defecto que parezcan aprobaciones, ni presentar la fecha de una página como si fuera una validación de vigencia.

### 3.3 Separación de los metadatos

El diseño conservará las siguientes distinciones:

- **Identidad técnica:** qué recurso se recuperó.
- **`Source Role`:** función asignada por la gobernanza de fuentes.
- **`Assessment Status`:** grado de evaluación registrado.
- **`Permitted Use`:** usos autorizados según la Trust Matrix y las reglas aplicables.
- **Estado de verificación runtime:** qué se pudo comprobar en la ejecución concreta.

El último campo es nuevo para el diseño de Change 04. No reemplaza ni modifica los estados de la Trust Matrix.

Por ejemplo, que una ejecución identifique correctamente KS-006 no demuestra por sí solo que el recurso recuperado sea la página gobernada definitiva, ni que todos los metadatos del registro estén verificados. Del mismo modo, un `PASS` de procedencia no debe convertir automáticamente un `UNVERIFIED` en un estado validado.

---

## 4. Reglas de decisión y fallos controlados

| Condición observada | Comportamiento requerido |
|---|---|
| Recurso identificado y mapeo KS verificado | Continuar la validación de gobernanza y evidencia. |
| Recurso identificado, pero sin mapeo KS verificable | No inventar el `KS-ID`; no presentarlo como fuente gobernada verificada. |
| Varias páginas candidatas para el mismo KS-ID sin reconciliación | Marcar la identidad gobernada como ambigua; no escoger una versión definitiva por inferencia. |
| `Source Role` o `Assessment Status` sin verificar | Preservar el estado no verificado y aplicar únicamente los usos permitidos que puedan establecerse por separado. |
| Fuente accesible pero no elegible para el uso solicitado | Excluirla como evidencia para ese uso. |
| Fragmento recuperado que no respalda la afirmación propuesta | No presentar la afirmación como un hecho demostrado por esa fuente. |
| Recuperación incompleta o truncada | Limitar la conclusión a la porción inspeccionada y comunicar la limitación cuando sea relevante. |
| Fuentes con metadatos o contenido contradictorios | Exponer el conflicto o detener la conclusión afectada; no resolverlo silenciosamente. |
| Metadatos necesarios no expuestos por CAPE | Registrar la limitación de la plataforma y no declarar que la comprobación se realizó. |

Estas reglas son consistentes con el principio de la Functional Specification: la respuesta debe tener exactamente el nivel de certeza que justifica la evidencia, y la elegibilidad depende de los campos gobernados, no de la mera accesibilidad.

---

## 5. Grounding mínimo requerido para Change 04

Change 04 establecerá la trazabilidad entre contenido y fuente, pero no debe atribuirse toda la responsabilidad del grounding a este cambio: Change 05 seguirá siendo responsable de la validación sistemática de las afirmaciones.

Para Change 04, el requisito mínimo será que una afirmación organizacional relevante no se presente como respaldada por una fuente sin poder identificar:

- el recurso realmente recuperado;
- su mapeo verificado, cuando exista;
- el fragmento o contenido que se utilizó;
- la relación entre ese contenido y la afirmación;
- las limitaciones de identidad, elegibilidad o recuperación que afecten a esa relación.

No se exige inventar un formato de cita visible al usuario ni introducir una sintaxis específica de `KS-ID`. Sí se exige que la evidencia de ejecución permita inspeccionar esa relación. Un `KS-ID` aislado no demuestra que una afirmación esté sustentada.

---

## 6. Criterios de aceptación

Change 04 no se considerará aceptado solo porque las instrucciones estén presentes en el Skill. Debe superar las comprobaciones siguientes:

| ID | Criterio | Condición de aceptación |
|---|---|---|
| **P04-01** | Identidad verificable | Cada fuente presentada como gobernada tiene una asociación demostrable con su recurso recuperado. |
| **P04-02** | Metadatos fieles | Los campos de gobernanza coinciden con el registro disponible o permanecen explícitamente no verificados. |
| **P04-03** | No inferencia | Títulos parecidos, contenido temático y resultados de búsqueda no se utilizan por sí solos para asignar un `KS-ID`. |
| **P04-04** | Control de duplicados | Las páginas duplicadas o discrepantes no se presentan como una única fuente gobernada sin reconciliación. |
| **P04-05** | Uso permitido | La identidad técnica no permite eludir las restricciones de elegibilidad o uso. |
| **P04-06** | Relación evidencia-afirmación | Las afirmaciones relevantes pueden rastrearse al contenido efectivamente utilizado. |
| **P04-07** | Fallo seguro | Cuando no puede verificarse un dato necesario, la respuesta comunica la limitación y no inventa metadatos. |
| **P04-08** | Evidencia reproducible | Se conserva el resultado de cada prueba, el Skill cargado y los datos de ejecución que estén disponibles. |

**Regla de aprobación:** Todos los criterios deben pasar en los escenarios aplicables. Si CAPE no proporciona los datos necesarios para verificar un criterio, ese criterio queda `NOT VERIFIABLE` y la aceptación completa permanece pendiente; la ausencia de datos no equivale a un pase.

---

## 7. Plan de verificación: siete casos existentes

Se reutilizarán los casos Q1, Q3, Q5, Q8, Q15, Q16 y Q19 que ya figuran en el Implementation Record. No se modificarán sus prompts para facilitar el resultado ni se crearán nuevas expectativas semánticas sin consultar el conjunto de pruebas vigente.

| Caso | Comprobación específica de procedencia |
|---|---|
| **Q1** | Comprobar que las fuentes utilizadas se asocian a identificadores verificables y que sus metadatos no se inventan. |
| **Q3** | Verificar la trazabilidad de KS-006 y KS-007; mantener la distinción entre la selección de fuentes, la identidad del recurso y la exactitud de las diez fases. |
| **Q5** | Inspeccionar la procedencia de KS-010 y comprobar que la afirmación adicional de escalamiento de seguridad pueda vincularse a evidencia directa o se identifique como no sustentada. |
| **Q8** | Aplicar las comprobaciones de identidad, metadatos y respaldo de afirmaciones al escenario original, sin alterar su intención. |
| **Q15** | Verificar el comportamiento de procedencia y el tratamiento de metadatos no confirmados en el escenario original. |
| **Q16** | Verificar el comportamiento de procedencia y el tratamiento de metadatos no confirmados en el escenario original. |
| **Q19** | Comprobar que el contenido recuperado para KG-003 no se convierta en evidencia elegible solo por ser accesible; preservar la limitación sobre DRPA/SOLDOC. |

Las comprobaciones de Q8, Q15 y Q16 se concretarán contra sus prompts y resultados de referencia existentes antes de ejecutar las pruebas. No se presupone aquí su contenido exacto.

### Evidencia que debe conservarse por caso

- Prompt original y conversación de prueba.
- Identidad o versión del Skill cargado, si CAPE la expone.
- Recursos recuperados y metadatos realmente visibles en la ejecución.
- `KS-ID` asignado y evidencia de su mapeo, si existe.
- Afirmaciones inspeccionadas y referencias al contenido que las respalda.
- Resultado por criterio: `PASS`, `FAIL` o `NOT VERIFIABLE`.
- Limitaciones de recuperación, duplicados o metadatos ausentes.

Los resultados históricos no se sobrescribirán. Los nuevos resultados se registrarán como ejecuciones distintas.

---

## 8. Dependencias, riesgos y controles

### Riesgo 1 — CAPE no expone metadatos suficientes
*Dependencia crítica.* El Skill puede solicitar trazabilidad, pero no necesariamente puede obtener el ID de página, versión, URL o fragmento exacto desde el conector.
- **Control:** Inspeccionar la salida real de las herramientas de CAPE antes de decidir el mecanismo de implementación. Si esos datos no están disponibles, documentar la limitación y ajustar el criterio solo mediante una decisión explícita de alcance; nunca simular trazabilidad.

### Riesgo 2 — Registros gobernados sin reconciliar
*Bloqueo de aceptación.* La correspondencia técnica de una página no resuelve la clasificación pendiente de KS-003/004/005/006/007/010 ni la ambigüedad de KS-015.
- **Control:** Mantener los valores actuales y solicitar la reconciliación por el proceso de gobernanza correspondiente. Change 04 no editará la Trust Matrix.

### Riesgo 3 — Confundir procedencia con grounding
Un recurso puede estar correctamente identificado y aun así no respaldar la afirmación generada.
- **Control:** Change 04 valida la línea de procedencia; Change 05 validará el soporte de las afirmaciones. Ambos resultados deben registrarse por separado.

### Riesgo 4 — Evidencia de ejecución insuficiente
Un texto de instrucciones actualizado no demuestra el comportamiento de CAPE.
- **Control:** Conservar salidas de ejecución y resultados de prueba; no declarar `PASS` a partir de una revisión textual.

---

## 9. Gobernanza y límites de implementación

La implementación deberá respetar estos controles:

- No cambiar la Trust Matrix, el Knowledge Inventory ni la Knowledge Taxonomy.
- No convertir campos `UNVERIFIED` en valores verificados.
- No ampliar el conjunto de siete fuentes elegibles.
- No elegir entre páginas duplicadas sin reconciliar la fuente gobernada.
- No presentar la trazabilidad de fuente como sustituto de Architecture Review, Security Review, CAB ni otras aprobaciones.
- No iniciar la regresión formal de 11 casos hasta completar los cambios posteriores previstos en la secuencia aprobada.

La documentación pública de Atlassian puede orientar la evaluación técnica de identificadores y versiones de páginas, pero cualquier uso de API, credenciales o conectores deberá ajustarse a las integraciones disponibles y autorizadas en CAPE.

---

## 10. Gateway: aprobación del diseño antes de implementar

El diseño de Change 04 está definido a nivel funcional. La siguiente fase debe comenzar con una comprobación técnica limitada de las capacidades reales de CAPE, sin modificar todavía el Skill activo.

El orden propuesto es:

1. Confirmar qué metadatos expone la salida de Confluence Search y Confluence Get Page.
2. Comprobar si existe una asociación fiable entre recursos recuperados y los registros KS.
3. Determinar qué criterios P04 pueden verificarse con los datos disponibles.
4. Identificar qué dependencias de gobernanza deben resolverse antes de una aceptación completa.
5. Solo después, redactar el cambio de instrucciones del Skill y ejecutar las pruebas focalizadas.

**Decisión requerida:** ¿Apruebas esta especificación funcional de Change 04, incluidos los criterios de aceptación y la regla de no declarar `PASS` cuando la trazabilidad no pueda verificarse? Tras tu aprobación, avanzaremos a la comprobación técnica de CAPE y sus metadatos disponibles, antes de tocar el Skill activo.
