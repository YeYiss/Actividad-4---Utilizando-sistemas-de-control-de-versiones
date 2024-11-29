const readline = require("readline-sync");

let tareas = []; // Lista de tareas

function agregarTarea() {
    const tarea = readline.question("Ingresa la tarea: ");
    tareas.push({ tarea, completada: false });
    console.log(`Tarea agregada: ${tarea}`);
}

// Ejemplo de uso
console.log("Historia 1: Agregar tareas");
agregarTarea();
console.log("Lista de tareas:", tareas);
