var exploitCode;
var disableCommands = false;

$(document).ready(function () {
    exploitCode = CodeMirror($("#usercode")[0], {
        'mode': 'python',
        'theme': 'the-matrix',
        'lineNumbers': true,
    });

    //$("#userterminal")[0].innerHTML += "<input type=\"text\" class=\"form-control\" id=\"inputCmd\" placeholder=\"Enter command\">";
    $('#inputCmd').keyup (function (e) {
        if (e.keyCode == 13 && !disableCommands) {
            var cmd = $("#inputCmd")[0].value;
            executeTerminalCommand(cmd);
            $("#inputCmd")[0].value = "";
        }
    });

    $("#exploit-container").slideUp(0);
});

function openTerminal() {
    $("#exploit-container").fadeOut("slow", function () {
        $("#terminal-container").fadeIn("slow");
    });

    $("#links-expl")[0].className = "";
    $("#links-term")[0].className = "active";
}
function openExploit() {
    $("#terminal-container").fadeOut("slow", function () {
        $("#exploit-container").fadeIn("slow");
    });

    $("#links-expl")[0].className = "active";
    $("#links-term")[0].className = "";
}

function executeTerminalCommand(cmd) {
    var bValid = 0;
    for (var i = 0; i < cmd.length; i++) {
        if (cmd[i] != ' ') {
            bValid++;
            break;
        }
    }
    if (bValid == 0)
        return;

    var term = document.getElementById("userterminal");
    term.scrollTop = term.scrollHeight;
    term.innerHTML += "<div class=\"clientMsg\">> " + cmd + "</div>";
    disableCommands = true;
    $.get('execCmd/',
        {cmd: cmd},
        function (data) {
            var term = document.getElementById("userterminal");
            term.innerHTML += "<div class=\"serverMsg\">" + data + "</div>";
            term.scrollTop = term.scrollHeight;
            disableCommands = false;
        }
    );
}

// POST FUNCTION FROM: http://stackoverflow.com/questions/133925/javascript-post-request-like-a-form-submit
function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for (var key in params) {
        if (params.hasOwnProperty(key)) {
            var hiddenField = document.createElement("input");
            hiddenField.setAttribute("type", "hidden");
            hiddenField.setAttribute("name", key);
            hiddenField.setAttribute("value", params[key]);

            form.appendChild(hiddenField);
        }
    }

    document.body.appendChild(form);
    form.submit();
}

function login() {

}
function signup() {

}
function logout() {

}