console.log(data);
const gelenVeriler = [
    { id: 1, name: "Öğe 1" },
    { id: 2, name: "Öğe 2" },
    { id: 3, name: "Öğe 3" }
];
document.addEventListener('DOMContentLoaded', () => {
    const veriListesi = document.getElementById('veriListesi');
    fetch('http://127.0.0.1:8000/api/data/')
        .then(response => response.json())
        .then(data => {
            data.forEach(veri => {
                console.log(data)
                const listItem = document.createElement('li');
                listItem.textContent = '${veri.id}: ${veri.fname}';
                veriListesi.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Hata:', error);
        });
});