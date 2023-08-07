document.addEventListener('DOMContentLoaded', function () {
    const calculateBtn = document.getElementById('calculate-btn');
    const resultElement = document.getElementById('result');

    calculateBtn.addEventListener('click', function () {
        const area = parseFloat(document.getElementById('area').value);
        const occupants = parseInt(document.getElementById('occupants').value);
        const buildingType = document.getElementById('building-type').value;
        const outdoorTemp = parseFloat(document.getElementById('outdoor-temp').value);
        const indoorTemp = parseFloat(document.getElementById('indoor-temp').value);

        // Calculate cooling load
        let coolingLoad = 0;
        if (buildingType === 'residential') {
            coolingLoad = 100 * occupants;
        } else if (buildingType === 'commercial') {
            coolingLoad = 150 * occupants;
        } else {
            resultElement.textContent = 'Invalid building type.';
            return;
        }

        const U = 30;
        const Q_conduction = U * area * (outdoorTemp - indoorTemp);
        const sensibleCoolingLoad = Q_conduction + coolingLoad;

        resultElement.textContent = `Sensible Cooling Load: ${sensibleCoolingLoad.toFixed(2)} W`;
    });
});
