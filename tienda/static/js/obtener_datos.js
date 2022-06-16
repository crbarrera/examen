$("#boton-usuarios").on("click", getUsers);

function getUsers() {
  $.ajax({
    url: "https://randomuser.me/api/?results=5&inc=name,location,picture",

    success: function (respuesta) {
    console.log(respuesta.results);

      var listaUsuarios = $("#lista-usuarios");
      
      $("#lista-usuarios").empty();
      $.each(respuesta.results, function (index, elemento) {     
        listaUsuarios.append(
        "<div>" +
            "<p> Nombre cliente: " +
            elemento.name.first +
            "</p>" +
            "<p> Pais cliente: " +
            elemento.location.country +
            "</p>" +
            "<img src='" +
            elemento.picture.large +
            "'/>" +
        "</div>"
        );
      });
    },
    error: function () {
      console.log("Error al cargar los datos");
    },
  });
}