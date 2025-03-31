MathJax = {
    tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['\\[', '\\]']]
    },
    startup: {
        ready: () => {
            MathJax.startup.defaultReady();
            const editorArea = document.querySelector(".cke_editable"); // Seleziona l'area di editing di CKEditor
            if (editorArea) {
                editorArea.addEventListener("input", function () {
                    MathJax.typesetPromise([editorArea]); // Esegui il rendering delle formule
                });
            }
        }
    }
};