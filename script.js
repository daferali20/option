// دالة لجلب بيانات عقود الأوبشن باستخدام Alpha Vantage
async function fetchOptionsData() {
    const proxyUrl = "https://cors-anywhere.herokuapp.com/";
    const apiUrl = "https://www.alphavantage.co/query?function=OPTION_CHAIN&symbol=TSLA&apikey=26E4LN8EWHQHLJSG";
    const url = 'https://corsproxy.io/?' + encodeURIComponent('https://www.alphavantage.co/query?function=OPTION_CHAIN&symbol=TSLA&apikey=26E4LN8EWHQHLJSG');

    try {
        const response = await fetch(proxyUrl + apiUrl);

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const data = await response.json();
        displayOptionsData(data);
    } catch (error) {
        console.error("Failed to fetch options data:", error);
        document.getElementById("errorMessage").style.display = "block";
    }
}

// دالة لعرض البيانات في الجدول
function displayOptionsData(data) {
    const options = data.optionChain.result[0].options[0].calls || [];
    const tableBody = document.getElementById("optionsTableBody");

    // تنظيف الجدول قبل إضافة البيانات
    tableBody.innerHTML = "";

    // تصفية العقود التي يكون حجمها أكبر من 5000 فقط
    options.filter(option => option.volume > 5000).forEach(option => {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${new Date(option.expirationDate * 1000).toLocaleDateString()}</td>
            <td>${option.volume}</td>
            <td>${option.contractSymbol}</td>
            <td>${option.bid.toFixed(2)}</td>
            <td>${option.ask.toFixed(2)}</td>
            <td>${option.change.toFixed(2)}</td>
        `;
        tableBody.appendChild(row);
    });

    console.log("Options data displayed successfully!");
}
