1. Prioridades de la semana
Change 04 — Verification & Formal Acceptance
Prioridad 1

Validación y evidencia de aceptación
- Verificar el paquete de evaluación Q11/Q12.
- Validar las correcciones R6–R8 contra sus resultados y evidencias correspondientes.
- Consolidar findings, gaps y acciones correctivas.
- Preparar el paquete de evidencia para aceptación formal.
  
  Change 05 — Claim-Level Grounding
  Prioridad 2
  
  Diseño funcional y criterios de validación
- Definir los requisitos de trazabilidad a nivel de cada claim.
- Establecer criterios para verificar que las afirmaciones estén respaldadas por sus fuentes.
- Delimitar el alcance de implementación.
- Identificar dependencias para regresión y preparación del piloto.
  
  Change 07 — Task Bank & Governance Gateway
  Prioridad 3
  
  Publicación, revisión y trazabilidad
- Confirmar el estado real de publicación del Task Bank v0.1.
- Verificar la documentación en Confluence.
- Dar seguimiento a la revisión de Nikko y aprobación de gobernanza.
- Identificar y documentar dependencias de trazabilidad pendientes.


---

2. Plan de trabajo: 9–13 de noviembre
Esta sería mi distribución recomendada para organizar la semana en el Kanban.
Lunes 9 — Change 04: Evidence Package Review
Objetivo: establecer exactamente qué evidencia existe y qué falta para completar la validación.
- Review the existing Q11/Q12 evaluation package and its required artifacts.
- Verify package integrity, document versions, provenance and traceability.
- Review the reported R6–R8 corrections against the corresponding requirements.
- Identify missing runtime evidence, unresolved findings and acceptance dependencies.
- Update the Change 04 validation checklist.
Entregable: Change 04 Evidence Inventory & Validation Gap Assessment.

Criterio de salida
 Inventario verificable de evidencia disponible, evidencia faltante y validaciones pendientes.
Martes 10 — Change 04: Q11/Q12 Evaluation Verification
Objetivo: verificar el comportamiento documentado y la evidencia de evaluación de los dos casos críticos.
- Review Q11: UiPath REFramework best practices and its Pending Validation source restriction.
- Review Q12: logging guidance and the absence of an identified candidate source.
- Compare expected behavior against the available evaluation outputs.
- Verify whether the coverage-honesty requirements are satisfied.
- Record discrepancies between expected and observed behavior.
- Document the evidence supporting each validation result.
El Pilot Specification establece que Q11 y Q12 son casos de cobertura crítica. Q11 debe rechazar el uso de una fuente pendiente de validación; Q12 debe reconocer que no existe una fuente candidata identificada para ese dominio. RPA_Development_Skill_Pilot_Specification_v0.1.docx
 RPA_Development_Skill_Pilot_Specification_v0.1.docx


Entregable: Q11/Q12 Verification Results.
Miércoles 11 — Change 04: R6–R8 Validation & Acceptance Findings
Objetivo: consolidar la validación de las correcciones y determinar qué falta para la aceptación formal.
- Verify R6–R8 corrections against their respective validation requirements.
- Review consistency between the corrected documentation and the available evaluation evidence.
- Consolidate validation findings and outstanding issues.
- Classify findings by severity, impact and required corrective action.
- Prepare the Change 04 acceptance evidence package.
- Document the remaining conditions preventing formal acceptance.
Entregable: Change 04 Validation Report & Acceptance Evidence Package.

Importante: no declarar Change 04 cerrado solamente porque las correcciones documentales estén aplicadas. La aceptación depende de que los criterios de validación y las evidencias correspondientes estén satisfechos.
Jueves 12 — Change 05: Claim-Level Grounding Design
Objetivo: convertir el concepto de grounding en requisitos funcionales verificables.

Aquí debemos trabajar sobre el diseño, sin modificar todavía el comportamiento del Candidate fuera del alcance autorizado.
- Define the claim-level grounding requirements and expected behavior.
- Establish the relationship between individual answer claims and their supporting source evidence.
- Define how supported, partially supported, unsupported and conflicting claims should be identified during validation.
- Establish source traceability requirements, including source identifiers and relevant provenance.
- Define validation criteria and acceptance conditions.
- Identify implementation dependencies and potential regression scenarios.
Entregable: Change 05 Claim-Level Grounding Requirements & Validation Criteria.

Hay una distinción importante: debemos preservar la inspectabilidad existente de P04–P06 en §4.3 del Candidate v0.1.1. No debemos introducir citas visibles ni un formato nuevo de atribución sin autorización. El diseño más amplio de grounding corresponde a Change 05.
Viernes 13 — Change 07 + Weekly Consolidation
Objetivo: desbloquear la publicación y revisión del Task Bank y consolidar el progreso semanal.
- Confirm the current publication status of Change 07 Task Bank v0.1.
- Verify whether the corresponding Confluence documentation is available and complete.
- Identify whether stakeholder review by Nikko is pending, ongoing or completed.
- Follow up on outstanding governance approval requirements.
- Review unresolved knowledge-source traceability and documentation dependencies.
- Update the Kanban with verified outcomes, outstanding blockers and next actions.
- Prepare a weekly progress summary covering Changes 04, 05 and 07.
Entregable: Task Bank Publication & Governance Status Report + Weekly Progress Summary.

No debemos marcar la publicación, revisión o aprobación como DONE hasta contar con evidencia de cada una.


