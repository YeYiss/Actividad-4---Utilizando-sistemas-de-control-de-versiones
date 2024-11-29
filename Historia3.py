function eliminarTarea() {
    if (tareas.length === 0) {
        console.log("No hay tareas en la lista.");
        return;
    }
    console.log("Tareas disponibles:");
    tareas.forEach((t, i) => console.log(`${i + 1}. ${t.tarea}`));
    const indice = parseInt(readline.question("Selecciona el número de la tarea a eliminar: ")) - 1;

    if (indice >= 0 && indice < tareas.length) {
        const tareaEliminada = tareas.splice(indice, 1);
        console.log(`Tarea eliminada: ${tareaEliminada[0].tarea}`);
    } else {
        console.log("Índice no válido.");
    }
}

// Ejemplo de uso
console.log("\nHistoria 3: Eliminar tareas");
eliminarTarea();
console.log("Lista actualizada de tareas:", tareas);
