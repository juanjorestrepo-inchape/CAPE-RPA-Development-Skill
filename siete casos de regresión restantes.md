
| Caso | Prompt de evaluación | Criterio principal |
| :--- | :--- | :--- |
| **Q1** | `How do I initiate an RPA project?` | KS-006, Primary |
| **Q3** | `What is the Project Intake Framework?` | KS-006 y las diez fases del ciclo de vida según el criterio de aceptación de Q3 |
| **Q5** | `What CAPTCHA / MFA requirements apply?` | KS-010, Primary |
| **Q8** | `My bot is involved in a critical incident – what's the playbook?` | KS-015, Supporting; declarar Role Ambiguity |
| **Q15** | `Which source should I consult for CAB requirements?` | Distinguir KS-006 y KS-007 según sus respectivos ámbitos |
| **Q16** | Prompt sintético de conflicto entre dos fuentes Primary | Aplicar la secuencia de resolución de conflictos; no escoger silenciosamente una fuente |
| **Q19** | `Explain the difference between DRPA and SOLDOC documentation.` | Declarar KG-003 y no inventar una distinción |


---

Cómo registrar cada ejecución
Conserva la respuesta completa, el registro de Load Skill, la identidad y versión del Skill y, cuando esté disponible, el hash SHA-256. Registra también cualquier ausencia de evidencia como Not available.

No consideraremos un caso aprobado únicamente porque la respuesta parezca correcta: debe satisfacer el comportamiento esperado y conservar evidencia suficiente para revisar su ejecución.

Gateway — siguiente validación: 

1. comienza con Q1, Q3 y Q5. Compárteme sus respuestas y logs, 
2. y los evaluaremos antes de continuar con Q8, Q15, Q16 y Q19. Así mantenemos una revisión controlada y evitamos acumular fallos sin identificar su origen.