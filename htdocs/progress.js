var val = 0

$(function () {
    $(document).ready(function () {
        $("#progressBar").progressbar({
            value: 0,
            max: 100,
            change: function () {
                $("#progressNumber").text($("#progressBar").progressbar("value") + "%");
            },
            complete: function () {
                $("#progressNumber").text($("#progressBar").progressbar("value") + "%　完了");
            }
        });
        var id = setInterval(function () {
            $.ajax({
                url: "counter.txt",
                dataType: "text",
                cache: false,
                })
                .then(
                    function (progress_number) {
                        val = Number(progress_number);
                        console.log("成功", val, progress_number);
                        $("#progressBar").progressbar("value", val);
                    },
                    function () {
                        console.log("失敗", val);
                    }
                );
            // $("#progressBar").progressbar("value", val);
            if (val >= 100) { clearInterval(id) }
            // 2000ミリ秒おきに更新
        }, 2000);
    });
});