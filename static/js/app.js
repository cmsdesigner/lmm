function addCommas(nStr) {
    nStr += '';
    x = nStr.split('.');
    x1 = x[0];
    x2 = x.length > 1 ? '.' + x[1] : '';
    var rgx = /(\d+)(\d{3})/;
    while (rgx.test(x1)) {
        x1 = x1.replace(rgx, '$1' + ',' + '$2');
    }
    return x1 + x2;
}


function status(dti, zip_dti) {

    var dti_diff = Number((dti - zip_dti.dti).toFixed(2))
    if (dti_diff >= 0) {
        return 1;
    } else if ((zip_dti_conv.std_dti < 0.2 && Math.abs(dti_diff) < zip_dti_conv.std_dti) || Math.abs(dti_diff) < 0.2) {
        return 0;
    } else {
        return -1;
    }
}


function update_results() {
    var dti = $("#slider-income").val() / $("#slider-loan").val();
    var zip_dti;
    if ($('#checkbox-fha').prop('checked')) {
        zip_dti = zip_dti_fha;
    } else {
        zip_dti = zip_dti_conv;
    }

    $('.result').hide();

    var cur_status = status(dti, zip_dti);

    if (cur_status == 1) {
        $('#result-good').show()
    } else if (cur_status == 0) {
        $('#result-doubt').show()
    } else {
        $('#result-bad').show();
    }
}