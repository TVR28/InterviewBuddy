import React, { useState } from 'react';
import Card from './Card';
import { Button, Modal } from 'rsuite';
import './CardGrid.css';
import NewCandidateForm from './NewCandidateForm';
import "rsuite/dist/rsuite.min.css";

const CardGrid = () => {
    const [cards, setCards] = useState([]);
    const [showCardForm, setShowCardForm] = useState(false);
    const [selectedCard, setSelectedCard] = useState(null);
    const [showCandidateForm, setShowCandidateForm] = useState(false);

    const addCard = (formData) => {
      const newCardId = cards.length + 1;
      const newCard = <Card key={newCardId} {...formData} title={`Card ${newCardId}`} onClick={() => handleClickCard(formData)} />;
      setCards([...cards, newCard]);
      setShowCandidateForm(false)
    };

    const handleClickCard = (formData) => {
        console.log('Card clicked');
        setShowCardForm(true);
        setSelectedCard(formData); // Set the selected card title
    };

    const handleCloseCardForm = () => {
        console.log('Closing form');
        setShowCardForm(false);
        setSelectedCard(null); // Reset the selected card
    };

    const modalDisplayStyle = showCardForm ? { display: 'block' } : { display: 'none' };
  
    console.log('showCardForm:', showCardForm); // Log the state here

    const [expandedResume, setExpandedResume] = useState(false);
    const [expandedDescription, setExpandedDescription] = useState(false);
    const [expandedTranscript, setExpandedTranscript] = useState(false);

    const toggleExpandedResume = () => {
        setExpandedResume(!expandedResume);
    };
    const toggleExpandedDescription = () => {
        setExpandedDescription(!expandedDescription);
    };
    const toggleExpandedTranscript = () => {
        setExpandedTranscript(!expandedTranscript);
    };
  
    return (
      <div className="grid">
        <div className="candidate-button">
            <Button className="add-button"onClick={() => setShowCandidateForm(true)} size="lg" style={{ fontWeight: 'bold' }}>Add New Candidate</Button>
        </div>
        <div className="grid-container-class">
            <div className="grid-container">
              {cards.map((card, index) => (
                <div key={index}>{card}</div>
              ))}
            </div>
        </div>
        {
            selectedCard && (
                <div className="pop-up-candidate-form">
                    <div>
                        <Button className='card-popup-close-button' onClick={handleCloseCardForm}>Close</Button>
                    </div>
                   <div> 
                        <Button className='card-popup-accept-button' onClick={handleCloseCardForm}>Accept</Button>
                        <Button className='card-popup-reject-button' onClick={handleCloseCardForm}>Reject</Button>
                   </div>

                    <div className="card-popup-content">
                    <h3>{selectedCard.name}</h3>
                    <p><strong>Email:</strong> {selectedCard.email}</p>
                    <p><strong>Role:</strong> {selectedCard.jobrole}</p>
                    <p><strong>Resume:</strong> {expandedResume ? selectedCard.resume : `${selectedCard.resume.slice(0, 100)}...`} {/* Display full resume if expanded, otherwise display a truncated version */}</p>
                        {selectedCard.resume.length > 100 && ( // Show "Read more" button if resume is longer than 100 characters
                            <button onClick={toggleExpandedResume}>{expandedResume ? 'Read less' : 'Read more'}</button>
                        )}
                    <p><strong>Job Description:</strong> {expandedDescription ? selectedCard.jobDescription : `${selectedCard.jobDescription.slice(0, 100)}...`} {/* Display full resume if expanded, otherwise display a truncated version */}</p>
                        {selectedCard.jobDescription.length > 100 && ( // Show "Read more" button if resume is longer than 100 characters
                            <button onClick={toggleExpandedDescription}>{expandedDescription ? 'Read less' : 'Read more'}</button>
                        )}
                    <p><strong>Interview Transcript:</strong> {expandedTranscript ? selectedCard.interviewTranscript : `${selectedCard.interviewTranscript.slice(0, 100)}...`} {/* Display full resume if expanded, otherwise display a truncated version */}</p>
                        {selectedCard.interviewTranscript.length > 100 && ( // Show "Read more" button if resume is longer than 100 characters
                            <button onClick={toggleExpandedTranscript}>{expandedTranscript ? 'Read less' : 'Read more'}</button>
                        )}
                    <p><strong>Analysis Report: </strong></p>
                   
                    </div>
                    
                </div>
            )
        }
        {
            showCandidateForm && (
                <div className='form-popup'>
                    <div>
                        <NewCandidateForm onSubmit={addCard}/>
                    </div>
                </div>
            )
        }
        
      </div>
    );
}

export default CardGrid;
