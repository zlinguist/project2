const tableData = data
const tbody = d3.select('tbody')
let filters = {}

function buildTable() {
    tbody.html('')

    data.forEach((row) => {
        const currentRow = tbody.append('tr')
        Object.values(row).forEach((value) => {
            let cell = currentRow.append('td')
            cell.text(value)
        })
    })
}

const handleClick = () => {
    d3.event.preventDefault()
    let filteredData = tableData;

    let latitdue_regionInput = d3.select("#latitude_region").property("value")
    let ratingInput = d3.select("#rating").property("value")
    let types1Input = d3.select("#types1").property("value")

    if (latitdue_regionInput) {
        filteredData = filteredData.filter((row) => row.latitude_region === latitude_regionInput)
    }
    if (ratingInput) {
        filteredData = filteredData.filter((row) => row.rating === ratingInput)
    }
    if (types1Input) {
        filteredData = filteredData.filter((row) => row.types1 === types1Input)
    }

    tbody.html('')

    filteredData.forEach((row) => {
        let currentRow = tbody.append('tr')
        Object.values(row).forEach((value) =>{
            let cell = currentRow.append('td')
            cell.text(value)
        })
    })
}

d3.selectAll('#submit').on('click', handleClick)
buildTable(tableData)