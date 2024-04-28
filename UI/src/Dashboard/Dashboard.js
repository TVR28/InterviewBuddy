// Dashboard.js

import React from 'react';
import CardGrid from './CardGrid';
import { Button, ButtonGroup, ButtonToolbar } from 'rsuite';
import "rsuite/dist/rsuite.min.css";
import "./Dashboard.css"

const Dashboard = () => {

  return (
    <div>
        <div className="header-div">
            <header className="header">
                <div >
                    <h2>Welcome John Doe!</h2>
                </div>
                {/* Add more dashboard content here */}
                <div>
                    <Button color="red" className="logout-button" size="lg" style={{ fontWeight: 'bold' }}>Logout</Button>
                </div>
            </header>
        </div>
    
        <div className="container">
            <CardGrid></CardGrid>
        </div> 
     
    </div>
  );
}

export default Dashboard;
