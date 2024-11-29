function verTareasPendientes() {
    const pendientes = tareas.filter(t => !t.completada);
    if (pendientes.length === 0) {
        console.log("No hay tareas pendientes.");
    } else {
        console.log("Tareas pendientes:");
        pendientes.forEach((t, i) => console.log(`${i + 1}. ${t.tarea}`));
    }
}

// Ejemplo de uso
console.log("\nHistoria 4: Ver tareas pendientes");
verTareasPendientes();
