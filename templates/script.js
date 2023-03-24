function calcular() {
    // Obtener los valores de PRETEST y POSTTEST ingresados por el usuario
    let pretest = document.getElementById("pretest").value.split(",").map(parseFloat);
    let posttest = document.getElementById("posttest").value.split(",").map(parseFloat);
  
    // Calcular las medias de PRETEST y POSTTEST
    let mean_pre = pretest.reduce((a, b) => a + b, 0) / pretest.length;
    let mean_post = posttest.reduce((a, b) => a + b, 0) / posttest.length;
  
    // Calcular la diferencia de medias
    let mean_diff = mean_post - mean_pre;
  
    // Verificar si hay una diferencia significativa
    if (pretest.toString() == posttest.toString()) {
      document.getElementById("resultado").innerHTML = "No hay una diferencia significativa entre el pretest y el posttest porque las medias son iguales.";
    } else if (mean_diff == 0) {
      document.getElementById("resultado").innerHTML = "No hay diferencias significativas porque las medias son iguales.";
    }
} 