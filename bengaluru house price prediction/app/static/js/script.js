document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("priceForm");

    form.addEventListener("submit", function(e) {
        const location = form.location.value.trim();
        const sqft = form.sqft.value.trim();
        const bath = form.bath.value.trim();
        const bhk = form.bhk.value.trim();

        let errors = [];

        if(location === "") errors.push("Please select a location.");
        if(sqft === "" || isNaN(sqft) || Number(sqft) <= 0) errors.push("Enter valid square feet.");
        if(bath === "" || isNaN(bath) || Number(bath) <= 0) errors.push("Enter valid number of bathrooms.");
        if(bhk === "" || isNaN(bhk) || Number(bhk) <= 0) errors.push("Enter valid BHK.");

        if(errors.length > 0) {
            e.preventDefault();
            alert(errors.join("\n"));
        }
    });
});
