        //warenkorb
        const warenAnzahlElement = document.querySelector(".warenAnzahl");

        const warenkorb = JSON.parse(localStorage.getItem("warenkorb"));

        if(warenkorb) warenAnzahlElement.innerHTML = warenkorb[Object.keys(warenkorb)[0]].length; 
        //