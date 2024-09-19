async function share_url() {
    const textValue = document.getElementById("text").value
    const endLife = new Date(document.getElementById("endLife").value)

    const response = await fetch("/share_url", {
        method: "POST",
        headers: {
            Accept: "application/json",
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ 
            text: textValue,
            endlife: endLife
        })
    });
    
    if (response.ok) {
        const html = await response.text();
    } else {
        console.log("Error: ", response.statusText);
    }
}