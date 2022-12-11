const btnDelete = document.querySelectorAll('.btn-delete')  //Selecciono todas las clases btn-delete y lo  guardo en una constante

if (btnDelete) 
{
    const btnArray = Array.from(btnDelete);  //El queryselectorall me devuelve una LISTA DE NODOS DE HTML por eso los recorro 
    
    btnArray.array.forEach((btn) => 
    {
        btn.addEventListener('click', (e) =>
        {       //El click toma la informacion del evento 
            if(!confirm('Are you sure you want to delete it?'))
            {
                e.preventDefault();     //Cancelo click y no envío petición al servidor caso contrario, se ejecuta la peticióny  se elimina
            }
        });
});
}