function calculate_difference_totals(container) {
    var actual_total = $(container).find('.costsActualTimeTotal').html();
    var developer_total = $(container).find('.costsDeveloperTimeTotal').html();
    var estimated_total = $(container).find('.costsTimeTotal').html();

    var developer_difference_total = actual_total / developer_total;
    var estimated_difference_total = actual_total / estimated_total;
    $(container).find('.costsDeveloperDifferenceTotal').html(developer_difference_total.toFixed(2));
    $(container).find('.costsEstimatedDifferenceTotal').html(estimated_difference_total.toFixed(2));
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
    calculate_difference_totals(container);
}
