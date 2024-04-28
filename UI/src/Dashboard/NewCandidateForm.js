// NewCandidateForm.js
import React, { useState } from 'react';
import { Button, Form, ButtonToolbar } from 'rsuite';

const NewCandidateForm = ({ onSubmit }) => {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        resume: '',
        interviewTranscript: '',
        jobDescription: ''
    });

    const handleChange = (fieldName, value) => {
        setFormData({
            ...formData,
            [fieldName]: value
        });
    };

    const handleSubmit = () => {
        onSubmit(formData); // Pass form data to parent component
        setFormData({
            name: '',
            email: '',
            resume: '',
            jobrole: '',
            interviewTranscript: '',
            jobDescription: ''
        });
    };

    return (
        <div className='form-popup-content'>
            <Form layout="horizontal">
                <Form.Group controlId="name-6">
                    <Form.ControlLabel>Candidate Name</Form.ControlLabel>
                    <Form.Control name="name" value={formData.name} onChange={value => handleChange('name', value)} />
                    <Form.HelpText>Required</Form.HelpText>
                </Form.Group>
                <Form.Group controlId="email-6">
                    <Form.ControlLabel>Email</Form.ControlLabel>
                    <Form.Control name="email" type="email" value={formData.email} onChange={value => handleChange('email', value)} />
                    <Form.HelpText tooltip>Required</Form.HelpText>
                </Form.Group>
                <Form.Group controlId="resume-6">
                    <Form.ControlLabel>Resume</Form.ControlLabel>
                    <Form.Control name="resume" rows={5} value={formData.resume} onChange={value => handleChange('resume', value)} componentClass="textarea" />
                    <Form.HelpText>Required</Form.HelpText>
                </Form.Group>
                <Form.Group controlId="jobrole-6">
                    <Form.ControlLabel>Role</Form.ControlLabel>
                    <Form.Control name="jobrole" value={formData.jobrole} onChange={value => handleChange('jobrole', value)} />
                    <Form.HelpText>Required</Form.HelpText>
                </Form.Group>
                <Form.Group controlId="interviewtranscript-6">
                    <Form.ControlLabel>Interview Transcript</Form.ControlLabel>
                    <Form.Control name="interviewTranscript" rows={5} value={formData.interviewTranscript} onChange={value => handleChange('interviewTranscript', value)} componentClass="textarea" />
                </Form.Group>
                <Form.Group controlId="jobdescription-6">
                    <Form.ControlLabel>Job Description</Form.ControlLabel>
                    <Form.Control name="jobDescription" rows={5} value={formData.jobDescription} onChange={value => handleChange('jobDescription', value)} componentClass="textarea" />
                    <Form.HelpText>Required</Form.HelpText>
                </Form.Group>
                <Form.Group>
                    <ButtonToolbar>
                        <Button onClick={handleSubmit} appearance="primary">Submit</Button>
                    </ButtonToolbar>
                </Form.Group>
            </Form>
        </div>
    );
};

export default NewCandidateForm;
