$(document).ready(function() {
    $("div.highlight").hover(
	function() {
	    $(this).css("display", "inline-block");
	    $(this).css("padding-bottom", "0");
	}, function() {
	    $(this).css("display", "block");
	    $(this).css("padding-bottom", "0.35em");
	}
    )
});
