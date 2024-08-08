package com.datorium.Datorium.API.Services;

import com.datorium.Datorium.API.DTOs.Message;
import org.springframework.stereotype.Service;

@Service

public class MessageService {
    public String add(Message message) {
        int choice = message.getChoice();
        switch (choice) {
            case 1:
                return "Hey, Choice 1 is to have a drink";
            case 2:
                return "Hey, Choice 2 is to have a drink and snacks";
            case 3:
                return "Hey, Choice 3 is to have a drink and full meal";
            default:
                return "Invalid choice, please select 1, 2, or 3";
        }
    }
}