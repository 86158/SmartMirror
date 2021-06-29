<script type="text/javascript">
           setTimeout(function(){
                window.location = "<?php getMyUrl(); ?>";
            }, 20000);

            $(function() {
    while( $('#fitin div').height() > $('#fitin').height() ) {
        $('#fitin div').css('font-size', (parseInt($('#fitin div').css('font-size')) - 1) + "px" );
    }
});
</script>