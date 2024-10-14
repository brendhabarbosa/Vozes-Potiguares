function exibirSubCategorias(e) {
    const ul = e.target.parentElement.getElementsByTagName('ul')[0]
 
    if (ul.style.display === 'block') {
       ul.style.display = 'none'
    } else {
       ul.style.display = 'block'
    }
 }
 
 document.getElementsByClassName('Cidades')[0].addEventListener('click', exibirSubCategorias)
 
 document.getElementsByClassName('Gêneros')[0].addEventListener('click', exibirSubCategorias)

 function abrirObraMenu(id) {
    const menu = document.getElementById(`menu-obras-${id}`)

    if (menu.style.display === 'block') {
      menu.style.display = 'none'
    } else {
       menu.style.display = 'block'
    }
 }
 
 
 document.getElementById('hamburguer').addEventListener('click', mostrarMenu)
 document.getElementById('fechar').addEventListener('click', mostrarMenu)