const fs = require("fs");

function guardarTareas() {
    fs.writeFileSync("tareas.json", JSON.stringify(tareas, null, 2));
    console.log("Tareas guardadas en tareas.json");
}

function cargarTareas() {
    if (fs.existsSync("tareas.json")) {
        const data = fs.readFileSync("tareas.json");
        tareas = JSON.parse(data);
        console.log("Tareas cargadas desde tareas.json");
    } else {
        console.log("No hay tareas guardadas.");
    }
}

// Ejemplo de uso
console.log("\nHistoria 5: Guardar y cargar tareas");
guardarTareas();
cargarTareas();
