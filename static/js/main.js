const btnDelete= document.querySelectorAll('.btn-delete');
if(btnDelete) {
  const btnArray = Array.from(btnDelete);
  btnArray.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      if(!confirm('Are you sure you want to delete it?')){
        e.preventDefault();
      }
    });
  });
} 

function buttonChange( that ){
  let val = that.value;
  if( that.id == 'holaNombre' ){
    let nombre = document.getElementById('Nombre').value;
    alert( val + ' ' + nombre + ' gracias por tu mensaje te mandaremos un correo lo mas antes posible' );
    window.location='/index2.html'; 
  }else{
    alert( val ); 
  }
}


const express = require('express')
const app = express()
const path = require('path')
const multer = require('multer')
const upload = multer({ dest: 'images/' })

app.get('/', (req, res) => {
  res.sendFile(path.resolve('index.html'))
})

app.post('/', upload.single('image'), (req, res) => {
  console.log(req.file)
  console.log(req.body.username)
  res.status(200)
})

app.listen(3005, () => {
  console.log('app en el puerto 3005')
})