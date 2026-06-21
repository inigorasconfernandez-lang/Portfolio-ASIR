# 🖥️ Implantación de Sistemas Operativos (ISO)

En esta sección se recopilan las prácticas y configuraciones clave relacionadas con la administración de sistemas operativos, enfocadas principalmente en la gestión avanzada de almacenamiento, tolerancia a fallos y optimización de discos.

---

## 🛠️ Prácticas Destacadas

### 1. Gestión de Volúmenes Lógicos (LVM)
* **Descripción:** Configuración y administración de espacios de almacenamiento flexibles mediante la abstracción del almacenamiento físico.
* **Habilidades clave:** Creación de Volúmenes Físicos (PV), Grupos de Volúmenes (VG) y Volúmenes Lógicos (LV). Redimensionamiento de particiones en caliente y extensión de sistemas de archivos.
* **Tecnologías:** Linux CLI (`pvcreate`, `vgextend`, `lvextend`), sistemas de archivos ext4/XFS.

### 2. Configuración de Sistemas RAID
* **Descripción:** Implementación de arreglos de discos redundantes para garantizar la alta disponibilidad y la tolerancia a fallos del sistema informático.
* **Tipos implementados:** RAID 0 (Rendimiento), RAID 1 (Espejo) y RAID 5 (Redundancia con paridad distribuida).
* **Tecnologías:** Herramienta `mdadm` en Linux, simulación de fallos de disco y reconstrucción de arrays.

### 3. Administración Multidiscos
* **Descripción:** Planificación, particionado y montaje de múltiples unidades de almacenamiento físico en un servidor.
* **Habilidades clave:** Creación de tablas de particiones (GPT/MBR), configuración del archivo `/etc/fstab` para el montaje automático y gestión de permisos a nivel de sistema de archivos.

---
> 💡 *Nota: Las memorias técnicas, capturas de pantalla o scripts específicos de cada práctica se irán subiendo dentro de subcarpetas asignadas en este mismo directorio.*
