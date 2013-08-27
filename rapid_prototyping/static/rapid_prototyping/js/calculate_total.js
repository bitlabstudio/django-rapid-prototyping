function calculate_average_for_column(container, item_cell, total_cell) {
    // Calculates the average over all `item_cell` values and adds it to the
    // `total_cell`.
    var total = 0;
    var count = 0;
    $(container).find(item_cell).each(function() {
        total += parseFloat($(this).html());
        count ++;
    });
    var average = total / count;
    console.log(average.toFixed(2));
    $(container).find(total_cell).html(average.toFixed(2));
}

function calculate_total_for_column(container, item_cell, total_cell) {
    // Creates a sum over all `item_cell` values and adds it to the
    // `total_cell`. We are currently not using this but it might be a better
    // value because calculating the average seems to have too many rounding
    // errors and result in a wrong value.
    var total = 0;
    $(container).find(item_cell).each(function() {
        total += parseFloat($(this).html());
    });
    $(container).find(total_cell).html(total.toFixed(2));
}

function calculate_total(container) {
    calculate_total_for_column(container, '.costsTime', '.costsTimeTotal');
    calculate_total_for_column(container, '.costsCosts', '.costsCostsTotal');
    calculate_total_for_column(container, '.costsDeveloperTime', '.costsDeveloperTimeTotal');
    calculate_total_for_column(container, '.costsDeveloperCosts', '.costsDeveloperCostsTotal');
    calculate_total_for_column(container, '.costsActualTime', '.costsActualTimeTotal');
    calculate_total_for_column(container, '.costsActualCosts', '.costsActualCostsTotal');
    calculate_average_for_column(container, '.costsDifference', '.costsDifferenceTotal');
}
