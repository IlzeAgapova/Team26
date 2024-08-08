package com.datorium.Datorium.API.DTOs;

public class Message {
    private int choice;

    public Message() {
    }

    public Message(int choice) {
        this.choice = choice;
    }

    public int getChoice() {
        return choice;
    }

    public void setChoice(int choice) {
        this.choice = choice;
    }
}
