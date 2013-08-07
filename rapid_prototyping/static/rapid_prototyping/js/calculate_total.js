function calculate_average_for_column(container, item_cell, total_cell) {
    // Calculates the average over all `item_cell` values and adds it to the
    // `total_cell`
    var total = 0;
    var count = 0;
    $(container).find(item_cell).each(function() {
        total += parseFloat($(this).html());
        count ++;
    });
    var average = total / count;
    $(container).find(total_cell).html(average);
}

function calculate_total_for_column(container, item_cell, total_cell) {
    // Creates a sum over all `item_cell` values and adds it to the
    // `total_cell`

    var total = 0;
    $(container).find(item_cell).each(function() {
        total += parseFloat($(this).html());
    });
    $(container).find(total_cell).html(total);
}

function calculate_total(container) {
    calculate_total_for_column(container, '.costsTime', '.costsTimeTotal');
    calculate_total_for_column(container, '.costsCosts', '.costsCostsTotal');
    calculate_total_for_column(container, '.costsDeveloperTime', '.costsDeveloperTimeTotal');
    calculate_total_for_column(container, '.costsActualTime', '.costsActualTimeTotal');
    calculate_total_for_column(container, '.costsActualCosts', '.costsActualCostsTotal');
    calculate_average_for_column(container, '.costsDifference', '.costsDifferenceTotal');
}
