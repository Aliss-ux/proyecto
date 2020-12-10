// Funcion que recibe los nombres y manda una notificacion de Alert 

function buttonChange( that ){
  let val = that.value;
  if( that.id == 'holaNombre' ){
    let nombre = document.getElementById('Nombre').value;
    alert( val + ' ' + nombre + ' gracias por tu mensaje te mandaremos un correo lo mas antes posible' );
    window.location='/index.html'; 
  }else{
    alert( val ); 
  }
}


//Funcion que recibe las sugerencias y las lleva a servidor local con npm


// const $form = document.querySelector('#contact')

// const $image = document.querySelector('#image')
// const $file = document.querySelector('#file')
// function renderImage(formData) {
//   const file = formData.get('image')
//   const image = URL.createObjectURL(file)
//   $image.setAttribute('src', image)
// }

// const $username = document.querySelector('#Nombre')
// function renderUsername(formData) {
//   const username = formData.get('Nombre')
//   $username.textContent = username
// }

// $file.addEventListener('change', (event) => {
//   const formData = new FormData($contact)
//   renderImage(formData)
// })

// $contact.addEventListener('submit', (event) => {
//   event.preventDefault()
//   const formData = new FormData(event.currentTarget)
//   renderUsername(formData)
//   fetch('/', {
//     method: 'POST',
//     body: formData,
//   })
// })


// admin



