import React from "react";
import CustomerView from "./CustomerView";
import StoreBack from "./StoreBack";

function Account({ customerArr, stores }) {

  const customerView = customerArr.map((customer) => {
    return <CustomerView key={customer.id}
      id={customer.id}
      name={customer.name}
      email={customer.email}
      age={customer.age}
      membership={customer.membership}
    />
  })
  console.log(customerArr)

  const storeMap = stores.map((store) => {
    return <StoreBack key={store.id}
      name={store.name}
      email={store.id}
      location={store.location}
    />
  })

  return (
    <div id='customerview'>
      {customerView}
      {storeMap}
    </div>
  );
}

export default Account;