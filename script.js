document.addEventListener('DOMContentLoaded', function() {
    fetch('./README.md')
        .then(response => response.text())
        .then(text => {
            const html = marked.parse(text);
            document.getElementById('readme-content').innerHTML = html;
        })
        .catch(error => {
            console.error('Error loading README.md:', error);
            document.getElementById('readme-content').innerHTML = '<p>Error loading README.md</p>';
        });
});