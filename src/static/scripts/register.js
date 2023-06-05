const form = document.querySelector("form")

form.addEventListener("submit",(e)=>{
    e.preventDefault()

    const email = form.email.value
    const password = form.password.value
    const confirm_password = form.confirm_password.value
    const phone = form.phone.value
    const title = form.title.valueOf
	
    const authenticated = authentication(email,password,confirm_password,phone,title)

    if(authenticated){
	    alert("correct")
    }else{
	    alert("wrong")
    }
})

// function for checking email, password, confirm password, phone and title

function authentication(email,password,confirm_password,phone,title){
    if(email === "mphokekana736@gmail.com" && password === "Baker24,." && confirm_password ==="Baker24,." && phone === "0810853596" && title === "Barra"){
	    return true
    }else{
	    return flase
    }
}
