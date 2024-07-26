document
.querySelector(".primary-button")
.addEventListener("click", async function() {
    const valueA = document.querySelector(".input-a").value
    const valueB = document.querySelector(".input-b").value
    let result = await eel.add_values(valueA, valueB)()
    document.querySelector(".result").innerText = result
})
