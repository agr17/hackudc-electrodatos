// Fade in
document.addEventListener('DOMContentLoaded', function () {
    const elements = document.querySelectorAll('.fade');
    const alreadyVisible = new Set(); // Conjunto para almacenar elementos que ya están visibles

    function checkVisibility() {
        elements.forEach(element => {
            if (alreadyVisible.has(element)) return; // Si el elemento ya está en el conjunto, salir

            const elementPosition = element.getBoundingClientRect();
            const screenHeight = window.innerHeight;

            // Verificar si la parte superior e inferior del elemento están dentro de la ventana
            if (elementPosition.top < screenHeight && elementPosition.bottom > 0) {
                element.classList.add('visible');
                alreadyVisible.add(element); // Agregar el elemento al conjunto de elementos visibles
            }
        });
    }

    function scrollHandler() {
        const scrollDirection = window.scrollY > this.lastScroll ? 'down' : 'up'; // Verificar dirección de scroll
        this.lastScroll = window.scrollY;

        if (scrollDirection === 'down') {
            checkVisibility();
        }
    }

    window.addEventListener('scroll', scrollHandler);

    // Verificar la visibilidad inicial al cargar la página
    checkVisibility();
});

// Dinámicamente ir subiendo el valor
document.addEventListener('DOMContentLoaded', function () {
    const fadeElement = document.querySelector('.fade');
    const valueSpan = document.querySelector('.valor');
    const finalPercentage = parseInt(valueSpan.textContent); // Valor final del porcentaje_top
    let alreadyVisible = false; // Variable para verificar si ya se mostró el valor por primera vez

    function incrementValue(start, end) {
        const increment = end > start ? 1 : -1;
        let current = start;

        const intervalId = setInterval(function() {
            current += increment;
            valueSpan.textContent = current;

            if (current === end) {
                clearInterval(intervalId);
            }
        }, 100); // Incrementar cada 100ms
    }

    function checkVisibility() {
        const elementPosition = fadeElement.getBoundingClientRect();
        const screenHeight = window.innerHeight;

        // Verificar si la parte superior e inferior del elemento están dentro de la ventana
        if (!alreadyVisible && elementPosition.top < screenHeight && elementPosition.bottom > 0) {
            incrementValue(0, finalPercentage);
            alreadyVisible = true; // Marcar como ya visible después de mostrar por primera vez
        }
    }

    window.addEventListener('scroll', checkVisibility);
    window.addEventListener('resize', checkVisibility);
    checkVisibility(); // Verificar la visibilidad inicial al cargar la página
});