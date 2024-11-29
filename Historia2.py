function marcarCompletada() {
    if (tareas.length === 0) {
        console.log("No hay tareas en la lista.");
        return;
    }
    console.log("Tareas disponibles:");
    tareas.forEach((t, i) => console.log(`${i + 1}. ${t.tarea} [${t.completada ? "✔" : "✘"}]`));
    const indice = parseInt(readline.question("Selecciona el número de la tarea a completar: ")) - 1;

    if (indice >= 0 && indice < tareas.length) {
        tareas[indice].completada = true;
        console.log(`Tarea completada: ${tareas[indice].tarea}`);
    } else {
        console.log("Índice no válido.");
    }
}

// Ejemplo de uso
console.log("\nHistoria 2: Marcar tarea como completada");
marcarCompletada();
console.log("Lista actualizada de tareas:", tareas);
