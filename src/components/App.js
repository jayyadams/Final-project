import { Route, Switch } from 'react-router-dom';
import React, { useState, useEffect } from "react";
import Account from './Account';
import Navbar from './Navbar';
import Login from './Login';
import StoreFront from './StoreFront';
import Inventory from './Inventory';
import Cart from './Cart';
import PlayerDetails from './PlayerDetails';
import RegistrationForm from './RegistrationForm';
import StoreLogForm from './StoreLogForm';
import LoginForm from './LoginForm';
import AccountManager from './AccountManager';
import CartImage from './CartImage';
import "../Stylesheet/index.css";
import About from './About';
import { SearchContext } from '../Helpers/Context';

function App() {
    // State variables
    const [players, setPlayers] = useState([]);
    const [stores, setStores] = useState([]);
    const [customerArr, setCustomer] = useState([]);
    const [loggedInID, setLoggedInID] = useState(1);
    const [loggedIn, setLoggedIn] = useState(false);
    const [searchTerm, setSearchTerm] = useState("");
    const [storeLogged, setStoreLoggedIn] = useState(false);

    // Fetch data from the server
    useEffect(() => {
        fetch('/stores')
            .then((resp) => resp.json())
            .then(setStores);
    }, []);

    useEffect(() => {
        fetch('/items')
            .then((resp) => resp.json())
            .then(setPlayers);
    }, []);

    useEffect(() => {
        fetch('/customers')
            .then((resp) => resp.json())
            .then(setCustomer);
    }, [storeLogged]);

    // Filtered customer IDs based on logged-in ID
    const filteredCustomerIDs = customerArr.filter((customer) => customer.id === loggedInID).map((customer) => customer.id);

    return (
        // Context provider for search term
        <SearchContext.Provider value={{ searchTerm, setSearchTerm }}>
            <header className='header'>
                {/* Header image */}
                <img src="./images/Header.png" alt='Header'></img>
            </header>
            <div id='bannerdiv'>
                {/* Navbar, Login, and Cart components */}
                <Navbar storeLogged={storeLogged} playersArr={players} />
                <Login loggedIn={loggedIn} storeLogged={storeLogged} setStoreLoggedIn={setStoreLoggedIn} />
                <Cart customer_id={filteredCustomerIDs[0]} />
            </div>
            <div id='maindiv'>
                {/* React Router Switch for routing */}
                <Switch>
                    <Route exact path='/Account_Manager'>
                        {/* Account Manager component */}
                        <AccountManager loggedInID={loggedInID} setLoggedIn={setLoggedIn} loggedIn={loggedIn} />
                    </Route>
                    <Route exact path="/">
                        {/* StoreFront component with search term and player data */}
                        <StoreFront searchTerm={searchTerm} playersArr={players} />
                    </Route>
                    <Route exact path="/players">
                        {/* Inventory component with player data */}
                        <Inventory playersArr={players} />
                    </Route>
                    <Route exact path="/customers">
                        {/* Account component with customer and store data */}
                        <Account customerArr={customerArr} stores={stores} />
                    </Route>
                    <Route exact path="/Register" component={RegistrationForm} />
                    <Route exact path="/CustomerLogin">
                        {/* Login Form component */}
                        <LoginForm setLoggedInID={setLoggedInID} setLoggedIn={setLoggedIn} loggedIn={loggedIn} />
                    </Route>
                    <Route exact path="/Cart" component={CartImage} />
                    <Route exact path="/StoreLogin">
                        {/* Store Login Form component */}
                        <StoreLogForm storeLogged={storeLogged} setStoreLoggedIn={setStoreLoggedIn} />
                    </Route>
                    <Route exact path="/About" component={About} />
                </Switch>
            </div>
        </SearchContext.Provider>
    );
}

export default App;