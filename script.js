 async function fetchOptionsData() {
            const ticker = document.getElementById("ticker").value.toUpperCase();
            if (!ticker) {
                alert("Please enter a valid stock ticker.");
                return;
            }

            // استخدام CORS Anywhere كخادم وسيط
            const proxyUrl = "https://cors-anywhere.herokuapp.com/";
            const apiUrl = `https://query1.finance.yahoo.com/v7/finance/options/${ticker}`;

            try {
                const response = await fetch(proxyUrl + apiUrl);
              if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
                const data = await response.json();
 console.log("Data fetched successfully:", data);
        } catch (error) {
            console.error("Failed to fetch options data:", error);
            alert("Failed to fetch options data. Please check the console for more details.");
        }
    }
                // التحقق من وجود بيانات
                if (!data || !data.optionChain || !data.optionChain.result) {
                    alert("No options data found.");
                    return;
                }

                const options = data.optionChain.result[0].options[0];
                const tbody = document.getElementById("optionsData");
                tbody.innerHTML = "";

                // عرض بيانات Call Options
                options.calls.forEach(option => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${new Date(option.expiration * 1000).toLocaleDateString()}</td>
                        <td>${option.strike}</td>
                        <td>${option.volume}</td>
                        <td>${option.openInterest}</td>
                        <td>Call</td>
                    `;
                    tbody.appendChild(row);
                });

                // عرض بيانات Put Options
                options.puts.forEach(option => {
                    const row = document.createElement("tr");
                    row.innerHTML = `
                        <td>${new Date(option.expiration * 1000).toLocaleDateString()}</td>
                        <td>${option.strike}</td>
                        <td>${option.volume}</td>
                        <td>${option.openInterest}</td>
                        <td>Put</td>
                    `;
                    tbody.appendChild(row);
                });
            } catch (error) {
                console.error("Error fetching options data:", error);
                alert("Failed to fetch options data.");
            }
        }
