//Акции
function op_act1(){
	var act=document.getElementById("action1");
	if(act.style.display=="block") {
		act.style.display="none";
	}
	else {
		act.style.display="block";
	}
}
function op_act2(){
	var act=document.getElementById("action2");
	if(act.style.display=="block") {
		act.style.display="none";
	}
	else {
		act.style.display="block";
	}
}

//Регистрация
function send(form_name){
	var check1= new RegExp("[0-9a-z_]+@[0-9a-z_^.]+\\.[a-z]{2,3}"); //логин(адрес почты)
	var check2= new RegExp("^[a-z0-9_]+[a-z0-9_]$"); //пароль
	if	((check1.test(login.value)==false)||(check2.test(password.value)==false)){
		if (check1.test(login.value)==false){
			document.getElementById("message1").style.display="inline-block";
		}
		if(check2.test(password.value)==false){
			document.getElementById("message").style.display="inline-block";
		}
	}
	else {document.forms[form_name].submit();}
}

//Доставка
var d=new Date();
var day=d.getDate();
var h=d.getHours();
function startTime(){
	if ((day==5)||(day==6)){
		if((h>=11)&&(h<22)){document.getElementById("txt").innerHTML="Возможность заказа с доставкой истечет через "+(22-h)+" часов";}
		else{document.getElementById("txt").innerHTML="На данный момент заказ с доставкой невозможно оформить";}
	}
	else{
		if((h>=11)&&(h<21)){document.getElementById("txt").innerHTML="Возможность заказа с доставкой истечет через "+(21-h)+" часов";}
		else{document.getElementById("txt").innerHTML="На данный момент заказ с доставкой невозможно оформить";}
	}
}

