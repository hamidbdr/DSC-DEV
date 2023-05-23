import LoginRegistation from '../LoginRegitrationPage/LoginRegistrationPage.jsx';
import Login  from './../Login/Login.jsx';
import Logout from './../Logout/Logout.jsx';
import { useState } from 'react';

function NavBar() {
    const [loguedState, setLogedState] = useState(false);
    const notregistred = true;
    return ( 
        <>
        <div>
            This is the Nav Bar Element
            {loguedState ? <Logout/> :  <Login/>}
            {notregistred && <LoginRegistation/>}
        </div>
        </>
     );
}

export default NavBar;