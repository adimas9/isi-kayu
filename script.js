document.addEventListener('DOMContentLoaded', () => {
    const woodTypeSelect = document.getElementById('woodType');
    const diameterInput = document.getElementById('diameter');
    const lengthInput = document.getElementById('length');
    const calcBtn = document.getElementById('calcBtn');
    const resultSection = document.getElementById('resultSection');
    const resultValue = document.getElementById('resultValue');
    const resultDetails = document.getElementById('resultDetails');

    // woodData is available globally from data.js
    if (typeof woodData === 'undefined') {
        console.error('Data kayu tidak ditemukan! Pastikan data.js dimuat.');
        alert('Gagal memuat database. Pastikan file data.js ada di folder yang sama.');
    } else {
        console.log('Database siap.');
    }

    calcBtn.addEventListener('click', calculateContent);

    function calculateContent() {
        if (typeof woodData === 'undefined') {
            alert('Database belum siap.');
            return;
        }

        const type = woodTypeSelect.value;
        const diameter = diameterInput.value.trim();
        const length = lengthInput.value.trim();

        if (!diameter || !length) {
            alert('Mohon isi diameter dan panjang kayu.');
            return;
        }

        // Logic Lookup using Strings to preserve "0.150"
        let foundValue = null;
        let message = '';

        if (woodData[type] && woodData[type][diameter]) {
            if (woodData[type][diameter][length] !== undefined) {
                // This is a STRING now, e.g., "0,150" or "0,87"
                foundValue = woodData[type][diameter][length];
            } else {
                message = `Panjang ${length} tidak ditemukan untuk diameter ${diameter} di database.`;
            }
        } else {
            message = `Diameter ${diameter} tidak ditemukan dalam database ${type === 'jati' ? 'Jati' : 'Mahoni'}.`;
        }

        if (foundValue !== null) {
            resultSection.classList.remove('hidden');
            resultDetails.innerHTML = `<p class="source-tag"><i class="fa-solid fa-database"></i> Data CSV: ${type === 'jati' ? 'Jati' : 'Mahoni'} (D:${diameter} / P:${length})</p>`;

            // Pass the Exact String to the animation function
            animateValue(resultValue, 0, foundValue, 800);

            if (window.innerWidth < 600) {
                resultSection.scrollIntoView({ behavior: 'smooth' });
            }
        } else {
            alert(`Data tidak ditemukan! \n${message}`);
            resultSection.classList.add('hidden');
        }
    }

    function animateValue(obj, start, endString, duration) {
        // endString is like "0,150" or "0,87"
        // Convert to number for animation
        const endNum = parseFloat(endString.replace(',', '.'));

        let startTimestamp = null;
        const step = (timestamp) => {
            if (!startTimestamp) startTimestamp = timestamp;
            const progress = Math.min((timestamp - startTimestamp) / duration, 1);
            // Ease out quartic
            const easeProgress = 1 - Math.pow(1 - progress, 4);

            const currentVal = (progress * (endNum - start) + start);

            // During animation, show 2-3 decimals depending on value
            // We use standard formatting during animation to avoid flickering
            let formattedCurrent = currentVal.toFixed(2).replace('.', ',');
            obj.innerHTML = formattedCurrent;

            if (progress < 1) {
                window.requestAnimationFrame(step);
            } else {
                // FORCE the exact string from database at the end
                // This ensures "0,150" shows as "0,150"
                obj.innerHTML = endString;
            }
        };
        window.requestAnimationFrame(step);
    }
});
