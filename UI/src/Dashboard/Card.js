// Card.js
import React from 'react';
import './Card.css';

const Card = ({name, email, jobrole, resume, interviewTranscript, jobDescription, title, onClick}) => {
  const handleClick = () => {
    if (onClick) {
      onClick(title); // Pass the title to the onClick function
    }
  };

  return (
    <div className="card" onClick={handleClick}>
        <h2>{name}</h2>
        <p>Email: {email}</p>
        <p>Role: {jobrole}</p>
        {/* <p>Resume: {resume}</p>
        <p>Interview Transcript: {interviewTranscript}</p>
        <p>Job Description: {jobDescription}</p> */}
    </div>
  );
};

export default Card;
