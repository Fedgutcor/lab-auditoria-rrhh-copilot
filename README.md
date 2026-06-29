# rrhh-copilot

> ⚠️ **REPOSITORIO DE EJEMPLO PARA AUDITORÍA — uso docente**
> Código de ejemplo con áreas de mejora plantadas a propósito para practicar auditoría asistida por IA.
> No es código de producción.

Asistente de IA que **ORDENA** hojas de vida para que un reclutador humano decida.

## Diseño (lo que está BIEN hecho a propósito)

- **Un humano siempre decide**: el sistema solo prioriza; no descarta a nadie de forma automática.
- **Sin atributos protegidos**: género, edad, nombre y foto se excluyen del scoring.
- **Procesamiento local**: no se envían datos personales a terceros.

## Cómo usar este repo en la clase

No tiene secretos commiteados ni decisiones automáticas ilegales. Pero sí tiene **brechas de gobernanza**: el modelo no se evalúa contra sesgo, no hay trazabilidad de las recomendaciones y arrastra una dependencia con vulnerabilidad conocida. Auditalo con Claude o Copilot: deberías llegar a **REQUIERE REVISIÓN** (hay altas, pero nada que bloquee de forma absoluta).
